// make a to-do list that utilizes local storage
// will need to also have HTML and CSS files I guess?

// establish all the DOM elements that I might need
const bodyElement = document.querySelector("body");
const textInput = document.getElementById("todo-input");
const submitButton = document.getElementById("submit-button");
const todoDiv = document.getElementById("item-container");
const todoList = document.getElementById("todo-list");
const todoForm = document.getElementById("todo-form");
// using this as an easy way to get/create new id's for my list items
let idCounter = 0;
// send this to localStorage with "todos" as its key
let storageItems = [];

todoForm.addEventListener("submit", (evt) => {
    evt.preventDefault();
    addItem(textInput.value);
    textInput.value = "";
});

const onStart = () => {
    if (localStorage.length >= 1) {
    let oldTodos = JSON.parse(localStorage.getItem("todos"));
    for (let i of oldTodos) {
        addItem(i.content);
    }
    }
}

const getId = () => {
    idCounter++;
    return idCounter;
}


// updates localStorage with whatever is in storageItems array
const addToLocalStorage = () => {
    localStorage.setItem("todos", JSON.stringify(storageItems));
}

// add an item to the to-do list
const addItem = (todo) => {
    // get id for item
    const myId = getId();
    // create new list item and give it a class, id, and it's content
    let newLi = document.createElement("li");
    let newButton = document.createElement("button");
    newButton.classList = "new-list-buttons";
    newLi.classList = "new-list-items";
    newLi.id = myId;
    newButton.id = myId;
    newButton.innerText = "Remove";
    newLi.innerText = todo;
    // append list item to list
    todoList.appendChild(newLi);
    newLi.appendChild(newButton);
    // add item to storage array so I can add it to localStorage
    storageItems.push({"id": newLi.id, "content": todo})
}

onStart();
