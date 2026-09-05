// BUGGY CODE:
// fetch('/playlist/delete/1/', {method: 'DELETE'}).then(res => console.log('Deleted'));
// Cause: Missing DOM manipulation logic in .then() block!

// FIXED CODE:
function deletePlaylist(playlistId) {
    fetch(`/playlist/delete/${playlistId}/`, {
        method: 'DELETE',
        headers: { 'X-CSRFToken': getCookie('csrftoken') }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'deleted') {
            const element = document.getElementById(`playlist-item-${playlistId}`);
            if (element) {
                element.remove(); // FIX: Explicitly remove DOM element on success
            }
        }
    })
    .catch(error => console.error('Error deleting playlist:', error));
}