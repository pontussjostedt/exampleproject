import config from '@/public-config';
import type { PageLoad } from './$types';
export const load: PageLoad = async ({fetch, depends}) => {
    console.log("SEND REQUEST")
    const res = await fetch(`${config.API_URL}/messages/`, {
        mode: "cors",
        headers: {
            "Origin": "http://localhost:3000" //Self origin
        }
        
    })

    depends("app:data") // https://kit.svelte.dev/docs/load

    const messages: string[] = await res.json() ?? []

    return {
        messages: messages
    }

}