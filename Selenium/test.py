import fateadm_api
import requests


fapi = fateadm_api.FateadmApi('309294', 'BdM+gl/hibSyJP+uPRTIayvz1T8Po4Kd', '109294', 'w+qA0pvUeRSj+P8zf8ikCkPG95tF8iQX')


content = requests.get('https://tushare.pro/captcha?action=login&unique_id=bdebc776149611e98231d00dd36710041547097327550678').content
with open('./images/img.jpg','wb') as f:
    f.write(content)

fapi.Predict('20400', content)