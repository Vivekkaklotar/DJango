// JavaScript fetch request with JSON response handling
function removeFromWatchLater(movieId) {
    fetch(`/watch-later/delete/${movieId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            document.getElementById(`movie-card-${movieId}`).remove();
            showNotification(data.message); // Displays dynamic success message banner
        }
    });
}