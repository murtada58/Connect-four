import { readable, writable } from 'svelte/store';
import * as eventTypesJSON from "../../eventTypes.json";

const DOMAIN = "127.0.0.1"; // "websockettictactoe.co.uk" // set to "127.0.0.1" or your servers ip if you want to host your own server you will need to change wss to ws as well unless you have a certificate
const PORT = "6789";

export const websocket = readable(new WebSocket(`ws://${DOMAIN}:${PORT}/`));

export const eventTypes = readable(eventTypesJSON);

export const user = writable({
  id: 0,
  name: "Guest",
  color: "#FFFFFF"
});
