import requests
import pandas as pd
import json
import yaml

pd.options.display.width = 0

class DataCollector:
    with open('config.yaml') as f:
        my_dict = yaml.safe_load(f)

    def send_payload(self):
        # send payload
        self.response = requests.post(self.my_dict['input_website'],
                                      headers=self.my_dict['header'], json=self.my_dict['input_data'])
        return self.response.text

    def load_data(self):
        # extracting data from jsons and loading into pandas DataFrame
        data = pd.json_normalize(json.loads(self.send_payload())['entries'])
        data['isActive'] = pd.Series()
        data['Role'] = pd.Series()
        data['Specialty'] = pd.Series()
        data['HCO_ID'] = pd.Series()
        data['Canton'] = pd.Series()
        data['Street'] = pd.Series()
        data['Zip_Code'] = pd.Series()
        for b, a in enumerate(json.loads(self.send_payload())['entries']):
            try:
                data.loc[b, 'isActive'] = a['professions'][0]['profession']['isActive']
                data.loc[b, 'Role'] = a['professions'][0]['profession']['textEn']
                data.loc[b, 'Specialty'] = a['professions'][0]['cetTitles'][0]['textEn']
                data.loc[b, 'HCO_ID'] = a['professions'][0]['cantons'][0]['canton']['id']
                data.loc[b, 'Canton'] = a['professions'][0]['cantons'][0]['canton']['textEn']
                data.loc[b, 'Street'] = a['professions'][0]['cantons'][0]['addresses'][0]['streetHouseNumber']
                data.loc[b, 'Zip_Code'] = a['professions'][0]['cantons'][0]['addresses'][0]['zipCity']
            except:
                data.loc[b, 'Street'] = a['professions'][0]['cantons'][1]['addresses'][0]['streetHouseNumber']
                data.loc[b, 'Zip_Code'] = a['professions'][0]['cantons'][1]['addresses'][0]['zipCity']
        data.rename(columns={'name':'lastName'}, inplace=True)
        data.drop(columns='professions', inplace=True)
        return data
