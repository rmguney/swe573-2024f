<script>
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input";
    import { Label } from "$lib/components/ui/label/index.js";
    import * as Sheet from "$lib/components/ui/sheet";
    import * as Tabs from "$lib/components/ui/tabs/index.js";
    import * as Card from "$lib/components/ui/card/index.js";
  
    let loginBar = false;
  </script>

<Button class="lg:px-12 hover:bg-rose-900" on:click={() => (loginBar = !loginBar)}>Sign In</Button>

<Sheet.Root bind:open={loginBar}>
    <Sheet.Overlay />
    <Sheet.Content side="right" class="w-96">
      <Sheet.Header>
        <Sheet.Close/>
      </Sheet.Header> 
      <div class="pt-8">
        <Tabs.Root value="login" class="w-full p-4">
          <Tabs.List class="grid w-full grid-cols-2">
            <Tabs.Trigger value="login">Login</Tabs.Trigger>
            <Tabs.Trigger value="register">Register</Tabs.Trigger>
          </Tabs.List>
          <Tabs.Content value="login">
            <Card.Root>
              <Card.Header>
                <Card.Title>Login</Card.Title>
                <Card.Description>
                  Do you already have an account? Login here!
                </Card.Description>
              </Card.Header>
              <Card.Content class="space-y-2">
                <div class="space-y-1">
                  <Label for="email">E-mail</Label>
                  <Input id="email" type="email" />
                </div>
                <div class="space-y-1">
                  <Label for="password">Password</Label>
                  <Input id="password" type="password" />
                  <small><a href="/" class="hover:text-rose-900" on:click={() => (loginBar = false)}>Forgot your password?</a></small>
                </div>
              </Card.Content>
              <Card.Footer>
                <Button class="hover:bg-rose-900" on:click={() => (loginBar = false)}>Login</Button>
              </Card.Footer>
            </Card.Root>
          </Tabs.Content>
          <Tabs.Content value="register">
            <Card.Root>
              <Card.Header>
                <Card.Title>Register</Card.Title>
                <Card.Description>
                  Create an account here to join the community!
                </Card.Description>
              </Card.Header>
              <Card.Content class="space-y-2">
                <div class="space-y-1">
                  <Label for="email">E-mail</Label>
                  <Input id="email" type="email"/>
                </div>
                <div class="space-y-1">
                  <Label for="username">Display Name</Label>
                  <Input id="username" type="username"/>
                </div>
                <div class="space-y-1">
                  <Label for="password">Password</Label>
                  <Input id="password" type="password" />
                </div>
              </Card.Content>
              <Card.Footer>
                <Button class="hover:bg-rose-900" on:click={() => (loginBar = false)}>Register</Button>
              </Card.Footer>
            </Card.Root>
          </Tabs.Content>
        </Tabs.Root>
      </div>
    </Sheet.Content>
  </Sheet.Root>