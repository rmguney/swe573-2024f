<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
    import Query from '$lib/components/query.svelte';

</script>
    
<div class="flex justify-center pt-8">
    <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
        <Card.Title class="p-4 text-2xl">
            Let's help you create a new thread!
        </Card.Title>

        <div class="p-4">
            <Textarea placeholder="First, we will start by giving it a title. That's what people will see on their feed." />
        </div>

        <div class="p-4 pt-0">
            <Textarea placeholder="Now let's give as much of a visual description as possible." />
        </div>

        <div class="flex flex-col lg:flex-row justify-between p-4 pt-0 w-full">

        <Query/>

        </div>

        <div class="p-4 pt-0">
            <input type="file" class="hover:text-rose-900 pt-4 lg:pt-0"/>
             </div>
    </Card.Root>
</div>
