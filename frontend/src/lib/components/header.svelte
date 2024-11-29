<script>
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import { Separator } from "$lib/components/ui/separator";
  import { toggleMode } from "mode-watcher";
  import Sun from "lucide-svelte/icons/sun";
  import Moon from "lucide-svelte/icons/moon";
  import * as Sheet from "$lib/components/ui/sheet";
  import Login from "$lib/components/login.svelte";
  import { activeUser } from "../../userStore";

  let navbar = false;
  let loginBar = false;
  let searchQuery = ""; // Bind to the search input
  let searchResults = []; // Holds filtered search results
  let allThreads = []; // Cache for all threads
  let loading = false; // Loading state
  let showDropdown = false; // Controls the visibility of the dropdown
  let highlightedIndex = -1; // For keyboard navigation

  // Function to fetch all threads initially
  async function fetchAllThreads() {
    loading = true;
    try {
      const response = await fetch("https://threef.vercel.app/api/thread/");
      if (response.ok) {
        allThreads = await response.json();
        searchResults = allThreads; // Initialize results with all threads
      } else {
        console.error("Failed to fetch threads");
      }
    } catch (error) {
      console.error("Error fetching threads:", error);
    } finally {
      loading = false;
    }
  }

  // Debounced filter function
  let debounceTimeout;
  function filterThreads() {
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(() => {
      const terms = searchQuery.trim().toLowerCase().split(/\s+/);
      if (terms.length < 1 || terms[0].length < 3) {
        searchResults = [];
        showDropdown = false;
        return;
      }

      searchResults = allThreads
        .map((thread) => {
          const content = `
            ${thread.title} 
            ${thread.description || ""} 
            ${thread.tags.join(" ")} 
            ${thread.material || ""} 
            ${thread.size || ""} 
            ${thread.shape || ""} 
            ${thread.color || ""} 
            ${thread.texture || ""} 
            ${thread.weight || ""} 
            ${thread.smell || ""} 
            ${thread.marking || ""} 
            ${thread.functionality || ""} 
            ${thread.period || ""} 
            ${thread.location || ""} 
          `.toLowerCase();

          const matchCount = terms.reduce(
            (count, term) => (content.includes(term) ? count + 1 : count),
            0
          );
          return { thread, matchCount };
        })
        .filter((item) => item.matchCount > 0)
        .sort((a, b) => b.matchCount - a.matchCount)
        .map((item) => item.thread);

      showDropdown = searchResults.length > 0;
    }, 300); // Adjust debounce delay as needed
  }

  // Highlight matching terms
  function highlightMatches(text, query) {
    const terms = query.trim().toLowerCase().split(/\s+/);
    return text.replace(new RegExp(`(${terms.join("|")})`, "gi"), "<mark>$1</mark>");
  }

  // Keyboard navigation
  function handleKeydown(event) {
    if (!showDropdown) return;

    if (event.key === "ArrowDown") {
      highlightedIndex = (highlightedIndex + 1) % searchResults.length;
    } else if (event.key === "ArrowUp") {
      highlightedIndex = (highlightedIndex - 1 + searchResults.length) % searchResults.length;
    } else if (event.key === "Enter") {
      if (highlightedIndex >= 0 && highlightedIndex < searchResults.length) {
        window.location.href = `/thread/${searchResults[highlightedIndex].id}`;
      }
    }
  }

  // Fetch threads on component mount
  fetchAllThreads();
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
  class="sticky top-0 flex justify-between items-center p-4 gap-2 w-full shadow-md bg-white dark:bg-black z-50"
  on:keydown={handleKeydown}
>
  <button on:click={() => (navbar = !navbar)} variant="outline">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 hover:text-rose-900 lg:hidden">
      <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" />
    </svg>
    <h1 class="text-2xl font-bold hover:text-rose-900 hidden lg:block">= Stufffinder</h1>
  </button>

  <!-- Search Bar -->
  <div class="flex items-center gap-2 relative" role="search">
    <label for="search-bar" class="sr-only">Search</label>
    <Input
      id="search-bar"
      type="search"
      placeholder="Search stuff"
      bind:value={searchQuery}
      class="w-96"
      on:input={filterThreads}
      on:focus={() => (showDropdown = searchQuery.trim().length >= 3)}
      aria-autocomplete="list"
      aria-expanded={showDropdown ? "true" : "false"}
      aria-owns="search-results"
      aria-controls="search-results"
    />
    {#if loading}
      <span class="absolute right-4 text-sm">Loading...</span>
    {/if}
    {#if showDropdown}
      <ul
        id="search-results"
        class="absolute top-full mt-2 w-full bg-white dark:bg-black shadow-md rounded-md overflow-hidden z-50"
        role="listbox"
        aria-label="Search Results"
      >
        {#each searchResults as result, index (result.id)}
          <!-- svelte-ignore a11y-role-has-required-aria-props -->
          <li
            role="option"
            class="p-2"
            class:hover={index === highlightedIndex ? "bg-gray-200 dark:bg-gray-700" : ""}
          >
            <button
              class="w-full text-left hover:bg-rose-900 cursor-pointer"
              on:click={() => (showDropdown = false)}
            >
              <a href={`/thread/${result.id}`} class="block">{@html highlightMatches(result.title, searchQuery)}</a>
            </button>
          </li>
        {/each}
        {#if searchResults.length === 0 && !loading}
          <!-- svelte-ignore a11y-role-has-required-aria-props -->
          <li role="option" class="p-2 text-gray-500 dark:text-gray-300">No results found</li>
        {/if}
      </ul>
    {/if}
  </div>

  <div class="flex items-center gap-2">
    {#if $activeUser}
      <span class="lg:mr-0 -mr-3">Welcome <a href="/" class="text-rose-900 hover:underline font-bold">{$activeUser}!</a></span>
      <Button class="lg:px-12 transition-all hover:bg-rose-900" on:click={() => activeUser.set(null)}>
        Logout
      </Button>
    {:else}
      <Login />
    {/if}

    <Button
      on:click={toggleMode}
      variant="outline"
      size="icon"
      class="bg-black dark:bg-white text-white dark:text-black hover:bg-rose-900 dark:hover:bg-rose-900 hover:text-white transition-colors duration-300"
    >
      <Sun class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-transform duration-300 dark:-rotate-90 dark:scale-0" />
      <Moon class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-transform duration-300 dark:rotate-0 dark:scale-100" />
    </Button>
  </div>
</div>

<Sheet.Root bind:open={navbar}>
  <Sheet.Overlay />
  <Sheet.Content side="left" class="w-48">
    <Sheet.Header>
      <Sheet.Title>
        <h3 class="text-8xl mt-8 mb-4 bold text-center">3F</h3>
      </Sheet.Title>
      <Sheet.Close />
    </Sheet.Header>
    <Separator />

    <nav class="mt-8 text-center">
      <ul class="space-y-8">
        <li><a href="/" class="block hover:text-rose-900 text-lg" on:click={() => (navbar = false)}>Home</a></li>
        {#if $activeUser}
        <li><a href="/create" class="block hover:text-rose-900 text-lg" on:click={() => (navbar = false)}>Create</a></li>
        {/if}
        <li><a href="/about" class="block hover:text-rose-900 text-lg" on:click={() => (navbar = false)}>About</a></li>
      </ul>
    </nav>
  </Sheet.Content>
</Sheet.Root>

<Sheet.Root bind:open={loginBar}>
  <Sheet.Overlay />
  <Sheet.Content side="right" class="w-96">
    <Sheet.Header>
      <Sheet.Close />
    </Sheet.Header>
    <Login />
  </Sheet.Content>
</Sheet.Root>
