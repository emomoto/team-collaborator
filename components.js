class TeamCollaboratorUI {
  static get env() {
    return {
      API_URL: process.env.API_URL,
    };
  }

  static initializeRealTimeUpdates() {
    console.log('Initializing real-time updates (This should be replaced with actual implementation)');
  }

  static taskList(tasks) {
    if (!Array.isArray(tasks)) {
      throw new Error('taskList expects an array of tasks');
    }

    const listElement = document.createElement('ul');
    listElement.className = 'task-list';

    tasks.forEach((task) => {
      if (!task || typeof task.title !== 'string') {
        console.error('Invalid task object', task);
        return;
      }
      const taskElement = document.createElement('li');
      taskElement.textContent = task.title;
      listElement.appendChild(taskElement);
    });
    return listElement;
  }

  static taskDetails(task) {
    if (!task || typeof task.title !== 'string' || typeof task.description !== 'string') {
      throw new Error('Invalid task object. Task must have a title and a description.');
    }

    const detailsElement = document.createElement('div');
    detailsSomeElement.className = 'task-details';
    detailsElement.innerHTML = `<h2>${task.title}</h2><p>${task.description}</p>`;
    return detailsElement;
  }

  static messageBoard(messages) {
    if (!Array.isArray(messages)) {
      throw new Error('messageBoard expects an array of messages');
    }

    const boardElement = document.createElement('div');
    boardElement.className = 'message-board';

    messages.forEach((message) => {
      if (typeof message !== 'string') {
        console.error('Invalid message content', message);
        return; // Skip this message
      }
      const messageElement = document.createElement('p');
      messageElement.textContent = message;
      boardElement.appendChild(messageElement); // Fixed line
    });
    return boardElement;
  }

  static addTaskForm() {
    const formElement = document.createElement('form');
    formElement.className = 'add-task-form';
    formElement.innerHTML = `
      <label for="taskTitle">Title: </label>
      <input type="text" id="taskTitle" name="title"><br>
      <label for="taskDesc">Description: </label>
      <textarea id="taskDesc" name="description"></textarea><br>
      <button type="submit">Add Task</button>
    `;
    formElement.onsubmit = (e) => {
      e.preventDefault();
      const title = document.getElementById('taskTitle').value.trim();
      const description = document.getElementById('taskDesc').value.trim();
      if (title && description) {
        console.log('Task submitted', { title, description });
      } else {
        console.error('Both Title and Description are required to add a task.');
      }
    };
    return formElement;
  }

  static addMessageForm() {
    const formElement = document.createElement('form');
    formElement.className = 'add-message-form';
    formElement.innerHTML = `
      <label for="messageContent">Message: </label>
      <textarea id="messageContent" name="content"></textarea><br>
      <button type="submit">Post Message</button>
    `;
    formElement.onsubmit = (e) => {
      e.preventDefault();
      const content = document.getElementById('messageContent').value.trim();
      if (content) {
        console.log('Message submitted', content);
      } else {
        console.error('Message content is required.');
      }
    };
    return formElement;
  }
}