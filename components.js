class TeamCollaboratorUI {
  static get env() {
    return {
      API_URL: process.env.API_URL,
    };
  }

  static taskList(tasks) {
    const listElement = document.createElement('ul');
    listElement.className = 'task-list';
    tasks.forEach((task) => {
      const taskElement = document.createElement('li');
      taskElement.textContent = task.title;
      listElement.appendChild(taskElement);
    });
    return listElement;
  }

  static taskDetails(task) {
    const detailsElement = document.createElement('div');
    detailsElement.className = 'task-details';
    detailsElement.innerHTML = `<h2>${task.title}</h2><p>${task.description}</p>`;
    return detailsElement;
  }

  static messageBoard(messages) {
    const boardElement = document.createElement('div');
    boardElement.className = 'message-board';
    messages.forEach((message) => {
      const messageElement = document.createElement('p');
      messageElement.textContent = message;
      boardElement.appendChild(messageElement);
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
      console.log('Task submitted');
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
      console.log('Message submitted');
    };
    return formElement;
  }
}