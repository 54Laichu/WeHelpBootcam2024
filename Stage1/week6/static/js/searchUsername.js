document.addEventListener('DOMContentLoaded', function() {
  const usernameInput = document.querySelector('#username-input');
  const searchButton = document.querySelector('#search-button');
  const searchResult = document.querySelector('#search-result');

  searchButton.addEventListener('click', async function() {
    const username = usernameInput.value;
    const result = await searchUsername(username);

		// 清空之前的結果
    searchResult.innerHTML = '';

    if (result && result.data) {
      const { name, username } = result.data;
      searchResult.appendChild(document.createTextNode(`${name} (${username})`));
    } else {
      searchResult.appendChild(document.createTextNode('No data'));
    }
  });

  async function searchUsername(username) {
    try {
      const response = await fetch(`/api/member?username=${username}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        return await response.json();
      } else {
        console.error('API request failed:', response.status);
        return null;
      }
    } catch (error) {
      console.error('Error:', error);
      return null;
    }
  }
});
