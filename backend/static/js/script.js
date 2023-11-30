$(document).ready(function() {
    function showPopupMessage(message, alertClass) {
        var alertDiv = $('<div class="alert ' + alertClass + '" role="alert">' + message + '</div>');
        $("#container-to-update").prepend(alertDiv);
        setTimeout(function() {
            alertDiv.slideUp();
        }, 10000);
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function handleSuccess(data, messageType, alertClass) {
        $("#container-to-update").html(data.html);
        $("#preview-submit-tasks").trigger('reset');
        $("#preview-submit-tasks").hide();

        var successMessage = "Task " + messageType + " successfully: " + data.title;
        showPopupMessage(successMessage, alertClass);
    }

    function handleError(error) {
        console.log(error);
        showPopupMessage("An error occurred.", "alert-danger");
    }

    $("#add-task-btn").click(function() {
        $.ajax({
            type: "POST",
            url: $(this).data("url"),  // Access the URL from the data attribute
            data: $("#add-task-form").serialize(),
            headers: { "X-CSRFToken": getCookie("csrftoken") },  // Include the CSRF token in the headers
            success: function(data) {
                if (data.html) {
                    // Update the task list container with the new HTML
                    $("#container-to-update").html(data.html);
                    window.location.href = data.home_url;  // Update with your actual URL
                } else if (data.error_message) {
                    // Display the error message
                    showPopupMessage(data.error_message, "alert-danger");
                } else {
                    console.error("Invalid response from the server");
                }
                $("#preview-submit-tasks").trigger('reset');
                $("#preview-submit-tasks").hide();
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
                handleSuccess(data, "deleted", "alert-danger");
            },
            error: function(error) {
                handleError(error);
            }
        });
    });

    $(document).on("click", ".edit-task", function() {
        var taskId = $(this).data("task-id");

        $.ajax({
            type: "POST",
            url: "/edit_task/" + taskId + "/",
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            success: function(data) {
                if (data.html) {
                    $("#container-to-update").html(data.html);
                    handleSuccess(data, "updated", "alert-warning");
                    window.location.href = data.home_url;
                } else {
                    console.error("Updated task list HTML not found in the response");
                }
            },
            error: function(error) {
                handleError(error);
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
    });
});

var jsonData = JSON.stringify(tasksData);
console.log(jsonData);

function truncateText(selector, maxLength) {
    var elements = document.querySelectorAll(selector);
    elements.forEach(function(element) {
        if (element.textContent.length > maxLength) {
            element.textContent = element.textContent.substr(0, maxLength) + '...';
        }
    });
}

truncateText('.description', 50);
