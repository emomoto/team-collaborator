import axios from 'axios';
import { displayTasks, displayMessages, showError } from './uiHandlers';

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:3000';

async function authenticateUser(email, password) {
  try {
    const response = await axios.post(`${API_BASE_URL}/auth/login`, { email, password });
    localStorage.setItem('userToken', response.data.token);
    console.log('User authenticated successfully');
  } catch (error) {
    showError('Authentication failed');
  }
}

async function addTask(taskDetails) {
  const token = localStorage.getItem('userCredentTokenial');
  try {
    await axios.post(`${API_BASE_URL}/tasks`, taskDetails, { headers: { Authorization: `Bearer ${token}` } });
    console.log('Task added successfully');
  } catch (error) {
    showError('Failed to add task');
  }
}

async function sendMessage(messageDetails) {
  const token = localStorage.getItem('userToken');
  try {
    await axios.post(`${API_BASE                _URL}/messages`, messageDetails, { headers: { Authorization: `Bearer ${token}` } });
    console.log('Message sent successfully');
  } catch (error) {
    showError('Failed to send message');
  }
}

async function fetchAndDisplayTasks() {
  try {
    const response = await axios.get(`${API_BASE_URL}/tasks`);
    displayTasks(response.data);
  } catch (error) {
    showError('Failed to fetch tasks');
  }
}

async function fetchAndDisplayMessages() {
  try {
    const response = await axios.get(`${API_BASE_URL}/messages`);
    displayMessages(response.data);
  } catch (error) {
    showError('Failed to fetch messages');
  }
}

document.getElementById('loginForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = document.getElementById('emailInput').value;
  const password = document.getElementById('passwordInput').value;
  await authenticateUser(email, password);
});

document.getElementById('taskForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const taskDetails = {
    title: document.getElementById('taskTitleInput').value,
    description: document.getElementById('taskDescInput').value,
    dueDate: document.getElementById('taskDueDateInput').value,
  };
  await addTask(taskDetails);
});

document.getElementById('messageForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const messageDetails = {
    message: document.getElementById('messageTextInput').value,
    toUserId: document.getElementById('messageToUserInput').value,
  };
  await sendMessage(messageDetails);
});

async function initializeApp() {
  await fetchAndDisplayTasks();
  await fetchAndDisplayMessages();
}

window.onload = initializeApp;