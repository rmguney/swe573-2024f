<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
    import Query from '$lib/components/query.svelte';

</script>
    
<div class="flex justify-center pt-8 px-4">
    <div class="w-full lg:w-2/3">
        <Card.Root>
            <Card.Title class="p-4 text-2xl">
                Let's help you post a new object!
            </Card.Title>

            <div class="p-4 pt-0">
                <Textarea placeholder="First, we will start by titling it. That's what people will see on their feed." />
            </div>

            <div class="p-4 pt-0">
                <Textarea placeholder="Now let's give as much of a description as possible. This will help people to identify it." />
            </div>

            <div class="p-4 pt-0 ">
                <Query/>
            </div>

            <div class="p-4 pt-0">
                <h3 class="text-md">
                    And lastly a photo or a video to go with it:
                </h3>
                <input type="file" class="hover:text-rose-900 pt-4 lg:pt-0"/>
            </div>
        </Card.Root>
    </div>
</div>
