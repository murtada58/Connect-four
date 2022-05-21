<script>
  import ActiveGamesRow from "./ActiveGamesRow.svelte";
  import Button from "./Button.svelte";

  let innerWidth = 0;
  let innerHeight = 0;
  $: showCreateGameButton = innerWidth > 800;

  const activeGames = [
    { name: 1 },
    { name: 2 },
    { name: 3 },
    { name: 4 },
    { name: 5 },
    { name: 6 },
    { name: 7 },
    { name: 8 },
    { name: 9 },
    { name: 10 },
    { name: 11 },
    { name: 12 },
  ];
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<div class="active-games-list-container container">
  <h2 class="active-games-list-title title active-text-color">Active Games</h2>

  <div class="active-games-list">
    {#each activeGames as activeGame}
      <ActiveGamesRow {...activeGame} />
    {/each}
  </div>
  {#if showCreateGameButton}
    <Button>Create Game</Button>
  {/if}
</div>

<style lang="scss">
  .active-games-list-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .active-games-list {
    grid-area: list;
    overflow-y: scroll;
    display: flex;
    flex-direction: column;
    height: 100%;
    gap: 0.5rem;
    padding: 0 0.5rem;
  }
</style>
