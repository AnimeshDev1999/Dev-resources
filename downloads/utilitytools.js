"usestrict";

////////// [[[Initalization of the variables]]] //////////

const weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
const yearMonths = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

////////// [[[Initalization of the DOM elements]]] //////////

const clockEl = document.querySelector(".Clock");
const calendarEl = document.querySelector(".Calendar");
const greetingEl = document.querySelector(".Greeting");

////////// [[[Logical Functions]]] //////////

// Digital clock
function timeUtility() {
  let hour = new Date().getHours();
  let min = new Date().getMinutes();
  let sec = new Date().getSeconds();
  clockEl.textContent = `${hour} : ${min} : ${sec}`;
} // setInterval(timeUtility, 1000);

// Digital calendar
function dayUtility() {
  let day = weekDays[new Date().getDay() - 1];
  let date = new Date().getDate();
  let month = yearMonths[new Date().getMonth()];
  let year = new Date().getFullYear();
  calendarEl.textContent = `${day} ${date} ${month} ${year}`;
} // dayUtility();

// Automated greeting
function greetingUtility() {
  let hour = new Date().getHours();
  let greet = "Morning";

  if (hour <= 12) {
    greet = "Morning";
  } else if (hour > 12 && hour <= 18) {
    greet = "Afternoon";
  } else {
    greet = "Evening";
  }

  greetingEl.textContent = `Good ${greet}`;
} // greetingUtility();

//Exexution

setInterval(timeUtility, 1000);
dayUtility();
greetingUtility();
