import requests

cookies = {
    "Cookie": "Hm_lvt_0c0239760addb3bfc082d763a601610a=1536825521,1536898492,1537148867,1537149548; Hm_lpvt_0c0239760addb3bfc082d763a601610a=1537149548; mongoMachineId=9326563; mongoMachineId=9326563; LEANOTE_FLASH=; Hm_lvt_adba6acce35cb0dd01685fd1014dd7d6=1536802150,1536825484,1537148853,1537149538; Hm_lpvt_adba6acce35cb0dd01685fd1014dd7d6=1537149538; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1536719911,1536802172,1536825484,1537149539; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537149548; LEANOTE_SESSION=c38a766cd4721f76c37133b9b14c26273987e11f-%00UsernameRaw%3ALeolulu%00%00Theme%3A%00%00NotebookWidth%3A170%00%00Username%3Aleolulu%00%00NoteListWidth%3A248%00%00Verified%3A1%00%00LeftIsMin%3A1%00%00Email%3A348699103%40qq.com%00%00_ID%3Ac5463d1bfb17278af5f3d09b14d1c282b9570b34359ca66663a85d6ea856eedf%00%00_TS%3A1537171294%00%00Logo%3Ahttps%3A%2F%2Fleanote.com%2Fpublic%2Fupload%2F561%2F5b45adc4ab644122f1001384%2Fimages%2Flogo%2F3d25bdb7b458e3b86b50572437f76971.png%00%00UserId%3A5b45adc4ab644122f1001384%00"
}

r = requests.get('https://leanote.com/note/5b987a58a56fd64c92000001',cookies= cookies,timeout=0.001)

print(
    requests.utils.dict_from_cookiejar(r.cookies)
)