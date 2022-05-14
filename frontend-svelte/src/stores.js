import { readable } from 'svelte/store';

const DOMAIN = "127.0.0.1"; // "websockettictactoe.co.uk" // set to "127.0.0.1" or your servers ip if you want to host your own server you will need to change wss to ws as well unless you have a certificate
const PORT = "6789";

export const websocket = readable(new WebSocket(`ws://${DOMAIN}:${PORT}/`));
export const websocketData = readable("", set => {
  websocket.onmessage = event => {
    set(JSON.parse(event.data));
  };

  return () => {
    websocket.onmessage = () => { };
  }
});

export const username = readable("", set => {
  return websocketData.subscribe(data => {
    data.type === "name" && set(data.name);
  });
});