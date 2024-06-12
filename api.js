import axios from 'axios';
const BASE_URL = process.env.REACT_APP_API_BASE_URL;
export const fetchTasks = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/tasks`);
    return response.data;
  } catch (error) {
    console.error("Error fetching tasks:", error);
    throw error;
  }
};
export const addTask = async (task) => {
  try {
    const response = await axios.post(`${BASE_URL}/tasks`, task);
    return response.data;
  } catch (error) {
    console.error("Error adding task:", error);
    throw error;
  }
};
export const updateTask = async (taskId, taskUpdates) => {
  try {
    const response = await axios.patch(`${BASE_URL}/tasks/${taskId}`, taskUpdates);
    return response.data;
  } catch (error) {
    console.error("Error updating task:", error);
    throw error;
  }
};
export const deleteTask = async (taskId) => {
  try {
    await axios.delete(`${BASE_URL}/tasks/${taskId}`);
  } catch (error) {
    console.error("Error deleting task:", error);
    throw error;
  }
};
export const fetchMessages = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/messages`);
    return response.data;
  } catch (error) {
    console.error("Error fetching messages:", error);
    throw error;
  }
};
export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${BASE_URL}/messages`, message);
    return response.data;
  } catch (error) {
    console.error("Error sending message:", error);
    throw error;
  }
};
export const fetchUsers = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/users`);
    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
};
export const createUser = async (user) => {
  try {
    const response = await axios.post(`${BASE_URL}/users`, user);
    return response.data;
  } catch (error) {
    console.error("Error creating user:", error);
    throw error;
  }
};
export const updateUser = async (userId, userUpdates) => {
  try {
    const response = await axios.patch(`${BASE_URL}/users/${userId}`, userUpdates);
    return response.data;
  } catch (error) {
    console.error("Error updating user:", error);
    throw error;
  }
};
export const deleteUser = async (userId) => {
  try {
    await axios.delete(`${BASE_URL}/users/${userId}`);
  } catch (error) {
    console.error("Error deleting user:", error);
    throw error;
  }
};