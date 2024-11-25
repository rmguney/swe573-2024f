<script>
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import { Separator } from "$lib/components/ui/separator";
  import { toggleMode } from "mode-watcher";
  import Sun from "lucide-svelte/icons/sun";
  import Moon from "lucide-svelte/icons/moon";
  import * as Sheet from "$lib/components/ui/sheet";
  import Login from '$lib/components/login.svelte';
  import { activeUser } from '../../userStore'; 

  let navbar = false;
  let loginBar = false;
</script>

<div class="sticky top-0 flex justify-between items-center p-4 gap-2 w-full shadow-md bg-white dark:bg-black z-50">
  <button on:click={() => (navbar = !navbar)} variant="outline">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 hover:text-rose-900 lg:hidden">
      <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" />
    </svg>
    <h1 class="text-2xl font-bold hover:text-rose-900 hidden lg:block">= Stufffinder</h1>
  </button>
<!--   <Input type="search" placeholder="Search stuff" class="max-w-xs" /> -->

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
      class="bg-black dark:bg-white text-white dark:text-black hover:bg-rose-900 dark:hover:bg-rose-900 hover:text-white transition-colors duration-300">
      
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
