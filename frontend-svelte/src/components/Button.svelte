<button class="button container active-text-color">
  <slot />
</button>

<style lang="scss">
  .button {
    font-size: 1rem;
    margin: 0;

    &:hover {
      cursor: pointer;
      background-color: rgba($color: #000000, $alpha: 0.6);
    }

    &:active {
      background-color: rgba($color: #333333, $alpha: 0.6);
    }
  }
</style>
