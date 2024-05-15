document.addEventListener('DOMContentLoaded', function () {
  const updateUsername = document.querySelector('#update-name');
  const updateButton = document.querySelector('#update-button');
  const updateResult = document.querySelector('#update-result');
  const welcomeMessage = document.querySelector('#welcome-message');

  updateButton.addEventListener('click', async function () {
    const name = updateUsername.value;
    const result = await updateName(name);

    // 清空之前的結果
    updateResult.innerHTML = '';

    if (result && result.ok) {
      updateResult.appendChild(document.createTextNode('更新成功'));
      welcomeMessage.textContent = `${name},歡迎登入系統`;
    } else {
      updateResult.appendChild(document.createTextNode('更新失敗'));
    }
  });

  async function updateName(name) {
    try {
      const response = await fetch('/api/member', {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name })
      });

      if (response.ok) {
        return await response.json();
      } else {
        console.error('Update failed:', response.status);
        return null;
      }
    } catch (error) {
      console.error('Error:', error);
      return null;
    }
  }
});
