import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL;

const handleError = (error, customMessage) => {
  if (error.response) {
    console.error(`${customMessage} - Response Error:`, error.response.data, error.response.status, error.response.headers);
  } else if (error.request) {
    console.error(`${customMessage} - Request Error:`, error.request);
  } else {
    console.error(`${customMessage} - Setup Error:`, error.message);
  }
  throw error.response ? error.response.data : new Error(customMessage);
};

export const fetchTasks = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/tasks`);
    return response.data;
  } catch (error) {
    handleError(error, "Error fetching tasks");
  }
};

export const addTask = async (task) => {
  try {
    const response = await axios.post(`${BASE_URL}/tasks`, task);
    return response.data;
  } catch (error) {
    handleError(error, "Error adding task");
  }
};

export const updateTask = async (taskId, taskUpdates) => {
  try {
    const response = await axios.patch(`${BASE_URL}/tasks/${taskId}`, taskUpdates);
    return response.data;
  } catch (error) {
    handleError(error, "Error updating task");
  }
};

export const deleteTask = async (taskId) => {
  try {
    await axios.delete(`${BASE_URL}/tasks/${taskId}`);
  } catch (error) {
    handleError(error, "Error deleting task");
  }
};

export const fetchMessages = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/messages`);
    return response.data;
  } catch (error) {
    handleError(error, "Error fetching messages");
  }
};

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${BASE_URL}/messages`, message);
    return response.data;
  } catch (error) {
    handleError(error, "Error sending message");
  }
};

export const fetchUsers = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/users`);
    return response.data;
  } catch (error) {
    handleError(error, "Error fetching users");
  }
};

export const createUser = async (user) => {
  try {
    const response = await axios.post(`${BASE_URL}/users`, user);
    return response.data;
  } catch (error) {
    handleError(error, "Error creating user");
  }
};

export const updateUser = async (userId, userUpdates) => {
  try {
    const response = await axios.patch(`${BASE_URL}/users/${userId}`, userUpdates);
    return response.data;
  } catch (error) {
    handleError(error, "Error updating user");
  }
};

export const deleteUser = async (userId) => {
  try {
    await axios.delete(`${BASE_URL}/users/${userId}`);
  } catch (error) {
    handleError(error, "Error deleting user");
  }
};