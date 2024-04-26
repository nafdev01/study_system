function djangoJsonToArray(djangoJson) {
    let data = JSON.parse(djangoJson);

    // Convert JSON to array
    let arrayData = Object.keys(data).map(key => data[key]);

    // Print array data
    return arrayData;

}

function dateTimeToFormattedString(dateTimeString) {
    // format date to show day of the week, date and time in 12 hour format with pm or am
    let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', hour12: true };
    return dateTimeString.toLocaleDateString('en-US', options);
}

function addMyEvent(student_id, arg, eventSocket) {
    silverBox({
        alertIcon: "warning",
        title: {
            text: "Add Event"
        },
        centerContent: true,
        text: "Enter the event details below to add a new event.",
        footer: "You can always edit the event details later.",
        showCloseButton: true,
        confirmButton: {
            text: "Add Event",
            onClick: function () {
                const name = document.querySelector("#id-name-input").value;
                const start_time = document.querySelector("#id-start-time-input").value;


                eventSocket.send(JSON.stringify({ "name": name, "start_time": start_time, "student_id": student_id, "ssup": "creating" }));
            }
        },
        cancelButton: {
            showButton: false,
        },
        input: [
            {
                label: "name",
                type: "text",
                placeHolder: "Enter the event name",
                maxLength: 255,
                id: "id-name-input",
            },
            {
                label: "start_time",
                type: "datetime-local",
                placeHolder: "Enter the event start time",
                value: arg.start.toISOString().slice(0, 16),
                id: "id-start-time-input",
            },
        ]
    })
}

function updateMyEvent(student_id, originalEvent, newEvent, eventSocket) {
    eventSocket.send(JSON.stringify({ "id": originalEvent.id, "name": originalEvent.title, "start_time": newEvent.start, "student_id": student_id, "ssup": "updating" }));
}

function deleteMyEvent(arg, calendar, EventSocket) {
    silverBox({
        alertIcon: "danger",
        title: {
            text: "Delete Event"
        },
        centerContent: true,
        text: `Are you sure you want to delete this event '${arg.event.title}'?`,
        footer: "You can't undo this action.",
        showCloseButton: true,
        confirmButton: {
            text: "Delete Event",
            onClick: function () {
                EventSocket.send(JSON.stringify({ "id": arg.event.id, "name": arg.event.title, "ssup": "deleting" }));
            }
        },
        cancelButton: {
            showButton: true,
        },
    })
}


function addedMyEvent(calendar, data) {
    console.log(data);
    start_date = new Date(data.start_time);

    calendar.addEvent({
        id: data.id,
        title: data.name,
        start: data.start_time,
        allDay: false,
    });

    silverBox({
        title: {
            alertIcon: "success",
            text: `Event '${data.name}' was created!`,

        },
        text: `Start Time: ${dateTimeToFormattedString(start_date)}`,
        centerContent: true,
        timer: 7500,
        animation: {
            duration: 5000,
        },
        position: "top-right",
    })
}

function updatedMyEvent(calendar, data) {
    console.log(data);
    silverBox({
        title: {
            alertIcon: "warning",
            text: `Event '${data.name}' was updated!`,

        },
        text: `Start Time: ${data.start_time}`,
        centerContent: false,
        timer: 7500,
        animation: {
            duration: 5000,
        },
        position: "top-right",
    })


}
function deletedMyEvent(calendar, data) {
    console.log(data);
    silverBox({
        alertIcon: "error",
        title: `You have deleted the event '${data.name}!`,
        centerContent: true,
        timer: 7500,
        animation: {
            duration: 5000,
        },
        position: "top-right",
    })
    calendar.getEventById(data.id).remove();
}
