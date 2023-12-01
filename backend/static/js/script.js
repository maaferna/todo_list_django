$(document).ready(function() {
    function showPopupMessage(message, alertClass) {
        var alertDiv = $('<div class="alert ' + alertClass + '" role="alert">' + message + '</div>');
        $("#container-to-update").prepend(alertDiv);
        setTimeout(function() {
            alertDiv.slideUp();
        }, 3000);
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
        
        // Check if the page was reloaded
        if (data.home_url) {
            window.location.href = data.home_url;  // Update with your actual URL
        }
    }

    function handleError(error) {
        console.log(error);
        showPopupMessage("An error occurred.", "alert-danger");
    }

    $("#add-task-btn").click(function() {
        $.ajax({
            type: "POST",
            url: $(this).data("url"),
            data: $("#add-task-form").serialize(),
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            success: function(data) {
                if (data.html) {
                    handleSuccess(data, "created", "alert-success");
                } else if (data.error_message) {
                    showPopupMessage(data.error_message, "alert-danger");
                } else {
                    console.error("Invalid response from the server");
                }
            },
            error: function(error) {
                console.log(error);
                handleError(error);
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
                console.log(error);
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
                    handleSuccess(data, "updated", "alert-warning");
                } else if (data.error_message) {
                    showPopupMessage(data.error_message, "alert-danger");
                } else {
                    console.error("Invalid response from the server");
                }
            },
            error: function(error) {
                console.log(error);
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
