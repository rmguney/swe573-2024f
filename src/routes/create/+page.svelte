<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
</script>
    
<div class="flex justify-center pt-8">
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
            <Card.Description class="p-4 text-2xl">
                Let's help you create a new thread!
            </Card.Description>
            <div>
                <div class="p-4">
            <Textarea placeholder="First, we will start by giving it a title. That's what people will see on their feed." />
        </div>
        <div class="p-4 pt-0">
            <Textarea placeholder="Now let's give as much of a visual description as possible." />
        </div>

            </div>
            <div class="items-center jutify-between p-4">
            <input type="file" class="hover:text-rose-900"/>
            select tags
            </div>
        </Card.Root>
</div>