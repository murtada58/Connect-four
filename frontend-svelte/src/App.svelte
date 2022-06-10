<script>
  import Header from "./components/Header.svelte";
  import ActiveGamesList from "./components/ActiveGamesList.svelte";
  import Chat from "./components/Chat.svelte";

  const secretCode = "randombackground";
  let currentlyTypedCode = new Array(secretCode.length).fill("");
  document.addEventListener("keydown", (event) => {
    currentlyTypedCode.push(event.key);
    currentlyTypedCode.shift();
    if (currentlyTypedCode.join("").toLowerCase() === secretCode) {
      fetch(
        "https://api.giphy.com/v1/gifs/random?api_key=MV4FwEbUqtZib1EuOVvjNiWx322Vt13O&tag=&rating=g"
      )
        .then((response) => response.json())
        .then((data) => {
          const gifUrl = data.data.images.original.url;
          document.body.style.backgroundImage = `url('${gifUrl}')`;
        });
    }
  });

  let innerWidth = 0;
  let innerHeight = 0;
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<div class="layout">
  <div class="header">
    <Header />
  </div>

  {#if innerWidth > 800}
    <div class="general-chat">
      <Chat chatRoom="general" />
    </div>
  {/if}

  <div class="content">
    <ActiveGamesList />
  </div>
</div>

<style lang="scss">
  .layout {
    display: grid;
    height: calc(100%); // 1 rem is the body padding
    width: 100%;
    grid-gap: var(--layout-gap);
    grid-template-columns: 1fr 2fr;
    grid-template-rows: auto 1fr;
    grid-template-areas:
      "header        header"
      "general-chat  content";
  }

  .header {
    grid-area: header;
    height: 5rem;
  }

  .general-chat {
    grid-area: general-chat;
    max-height: calc(100vh - 10rem);
  }

  .content {
    grid-area: content;
    max-height: calc(100vh - 10rem);
  }

  @media only screen and (max-width: 800px) {
    .layout {
      grid-template-areas:
        "header        header"
        "content  content";
    }
  }
</style>
