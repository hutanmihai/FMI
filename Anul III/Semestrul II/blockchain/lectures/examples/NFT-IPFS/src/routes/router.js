import React from "react"

import Path from "./path"
import {Welcome} from "../components/Welcome.js"
import {Wallet} from "../components/Wallet"
import {Events} from "../components/Events"
import {IpfsLoader} from "../components/IpfsLoader"

const routes = [
    { path: Path.WELCOME, element: <Welcome /> },
    { path: Path.WALLET, element: <Wallet /> },
    { path: Path.HOME, element: <Welcome /> },
    { path: Path.EVENTS, element: <Events /> },
    { path: Path.IPFS, element: <IpfsLoader /> },

]

export default routes