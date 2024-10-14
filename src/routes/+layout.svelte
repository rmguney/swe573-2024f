<script>
        import { ModeWatcher } from "mode-watcher";
        import Header from '$lib/components/header.svelte';
        import { onMount } from 'svelte';

        onMount(() => {
        if (performance.navigation.type === 1 && window.location.pathname !== '/') {
                window.location.href = '/';
        }
        });
</script>

        
<style>
        .shifting::before {
          content: "";
          z-index: -1; 
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background-color: #1a1a1b;
          background-image:
              radial-gradient(circle farthest-corner at 25% 25%, #8a4843, transparent 50%),
              radial-gradient(circle at 75% 75%, #5b7d8a, transparent 50%), 
              radial-gradient(circle at 50% 50%, #2c5f5a, transparent 50%), 
              radial-gradient(circle at 25% 75%, #627978, transparent 50%),
              radial-gradient(circle at 75% 25%, #E5A39E, transparent 50%),
              radial-gradient(circle at 50% 100%, #484854ff, transparent 50%);
          animation: bg-change 10s ease-in-out infinite;
          filter: blur(999px);
        }
        
        @keyframes bg-change {
          0%, 100% {
              filter: hue-rotate(0deg);
          }
          50% {
              filter: hue-rotate(-45deg);
          }
        }
</style>

<body>
        <ModeWatcher />  
        <main>
         <Header/>
         <slot/>
        </main>

</body>
<div class="shifting" />