document.addEventListener('DOMContentLoaded', function () {
  const deleteButtons = document.querySelectorAll('.delete-button');

  deleteButtons.forEach(button => {
    button.addEventListener('click', function () {
      const messageId = this.dataset.messageId;
      confirmDelete(messageId);
    });
  });

  function confirmDelete(messageId) {
    if (confirm("確定要刪除這則留言嗎?")) {
      let formData = new URLSearchParams();
      formData.append('message_id', messageId);

      fetch("/deleteMessage", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData.toString()
      })
      .then(response => {
        if (response.ok) {
          window.location.reload();
        }
      });
    }
  }
});
