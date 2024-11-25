<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';

  let user;
  let error;

  onMount(async () => {
    const userId = $page.params.id;
    try {
      const response = await fetch(`/api/user/${userId}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      user = await response.json();
    } catch (err) {
      error = err.message;
    }
  });
</script>

{#if error}
  <p>Error: {error}</p>
{:else if !user}
  <p>Loading...</p>
{:else}
  <div>
    <h1>{user.name}</h1>
    <p>{user.email}</p>
    <!-- Add more user details here -->
  </div>
{/if}
