import config from '@/public-config';
import type { PageLoad } from './$types';
export const load: PageLoad = async ({fetch}) => {
    console.log("SEND REQUEST")
    const res = await fetch(`${config.API_URL}/messages/`, {
        mode: "cors",
        headers: {
            "Origin": "http://localhost:3000" //Self origin
        }
        
    })
    const json = res.json()
    console.log(json)
    return json 

}