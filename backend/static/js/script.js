$(document).ready(function() {
    // Function to get the CSRF cookie value
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Check if this cookie string begins with the name we want
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $("#add-task-btn").click(function() {
        $.ajax({
            type: "POST",
            url: $(this).data("url"),  // Access the URL from the data attribute
            data: $("#add-task-form").serialize(),
            headers: { "X-CSRFToken": getCookie("csrftoken") },  // Include the CSRF token in the headers
            success: function(data) {
                $("#container-to-update").html(data.html);
                $("#preview-submit-tasks").trigger('reset');
                $("#preview-submit-tasks").hide(); // Add this line to hide the form after submission
                // Display the success message
                var alertDiv = $('<div class="alert alert-success" role="alert">' + data.message + '</div>');
                $("#container-to-update").prepend(alertDiv);

                // Automatically hide the alert after 3 seconds (adjust as needed)
                setTimeout(function() {
                    alertDiv.slideUp();
                }, 3000);
                },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $(document).on("click", ".delete-task", function() {
        var taskId = $(this).data("task-id");
    
        $.ajax({
            type: "POST",
            url: "/delete_task/" + taskId + "/",
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            success: function(data) {
                console.log(data.html);
    
                // Use native JavaScript to update the container
                var containerToUpdate = document.getElementById("container-to-update");
                if (containerToUpdate) {
                    containerToUpdate.innerHTML = data.html;
                } else {
                    console.error("Container not found");
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    
});


var tasksData = [];
var taskItems = document.querySelectorAll('.task-item');

taskItems.forEach(function(taskItem) {
    tasksData.push({
        id: taskItem.getAttribute('data-task-id'),
        title: taskItem.querySelector('h4').innerText,
        description: taskItem.querySelector('p:nth-child(2)').innerText,
        priority: taskItem.querySelector('p:nth-child(3)').innerText,
        effort: taskItem.querySelector('p:nth-child(4)').innerText,
        // Add more properties as needed
    });
});

// Send the JSON object as a response
var jsonData = JSON.stringify(tasksData);
console.log(jsonData);  // You can use this data as needed, for example, sending it via AJAX


function truncateText(selector, maxLength) {
    var elements = document.querySelectorAll(selector);
    elements.forEach(function(element) {
        if (element.textContent.length > maxLength) {
            element.textContent = element.textContent.substr(0, maxLength) + '...';
        }
    });
}

truncateText('.description', 50);