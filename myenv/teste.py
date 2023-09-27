# import requests

# url = "https://api.firstlanguage.in/api/classify"

# payload = {"input": {
#         "text": "Gasoline and diesel oil prices are already at their highest levels in 2023 and are expected to rise further by the end of the year. The tendency, according to experts interviewed by Poder360, is for values to remain under pressure, mainly due to movements in the external scenario, such as restrictions in the supply of oil and increased demand. Last Tuesday (September 5), Russia and Saudi Arabia, two of the largest global powers in the sector, announced the maintenance of oil production cuts. The Arabs extended the daily supply reduction of 1 million barrels for another 3 months. The Russians cut exports by 300 thousand barrels per day. The tightness in oil supply directly impacts prices. It's the law of the market: with less product available, the price rises. The Brent barrel, which is the international reference, reached US$90.60 on Wednesday (September 6) - at the highest price since November 2022. The value of a barrel of oil is one of the main components in the formation of fuel prices . It started the year at US$82. On June 12, it reached the lowest level of the year: US$71.80. While supply is low, global demand should be stable or even growing. A lot depends on China's behavior. According to the managing partner of CBIE (Brazilian Infrastructure Center), Adriano Pires, the Chinese economy has grown, but not as much as the market expected. “What we should have is a scenario of increased fuel prices or stability, at least. The size of this depends largely on China's behavior. It is not possible, given the current situation, to project a reduction in prices, unless we see a slowdown in the global economy,” he stated. With expectations in China and other factors, analysts predicted a barrel of US$ 100 by the end of the year. This scenario currently seems less likely. “The exchange rate is stabilized, unless an extraordinary event occurs. The barrel is expected to grow in the 2nd half of the year, with restricted supply, inflation and growth of the Chinese economy, but we have to see the size of the growth”, says Pires. This scenario adds to the internal problems, which have already raised prices. Last week, diesel oil exceeded R$ 6. The average price of gasoline in the country was R$ 5.87, having for the 2nd week in a row the highest value recorded in the year by the ANP (National Petroleum and Petroleum Agency) survey. Natural gas). Due to high prices, the market is already projecting a reduction in gasoline consumption. For September, demand is expected to fall 3.4%, the first drop since the pandemic. The reason is the increase in ethanol consumption, which has become more competitive, says Amance Boutin, fuel specialist at Argus, a company that specializes in producing reports and analyzes for the fuel market. “The outlook for gasoline demand in Brazil for the rest of the year is downward, following an uninterrupted increase in consumption since Covid. Consumers are switching to hydrated ethanol, which is expected to increase consumption by 15%. The internal supply perspective does not change much. With the drop in demand, we should have more slack in supply,” he says. Diesel has a worse scenario. The case of diesel is the most delicate. The price has been climbing for 6 weeks and is now at its highest value since February. And it will rise further: last Tuesday (September 5), the government resumed charging federal taxes on fuel. The PIS/Cofins rate will be partial, but will increase progressively until January. “The current situation and in the coming months is a tightening of oil supply. But the global market still finds an ample supply of gasoline. In the case of diesel, it has a greater impact. The national supply capacity is already fully employed and you need to resort to external products. And there is a tendency for prices to rise in the international diesel market”, says Amance Boutin. The Argus expert recalls that part of the diesel imported by Brazil is Russian, which arrives in the country at a lower cost. “[This diesel] comes with a big discount for Brazil to be able to sell the product in large markets, as we have no restrictions here to bring Russian products. But with the extension of Russia's cut, this should impact the value of their diesel.” Diesel prices had been falling since the beginning of the year, which was accentuated after the announcement of the new policy by Petrobras (BVMF:PETR4), which abandoned the PPI (Import Parity Price) in May. It even dropped R$0.60 at the pumps from May to July alone. Since then, values have been rising every week. First, due to the internal supply crisis that reduced diesel stocks in the country due to the drop in imports. With the prices being charged by Petrobras, bringing fuel from abroad was not paying off. And around 25% of the diesel consumed in the country is imported. The result: some stations had difficulty purchasing. With little supply, prices rose. Then, there was the Petrobras adjustment, announced on August 15, which increased diesel prices at refineries by 25%. It resolved most of the gap, which, however, still persists. The current values of the state-owned company are 14% below international prices (it reached a 30% lag at the beginning of August), indicates a report by Abicom (Brazilian Association of Fuel Importers) released last Wednesday (September 6). Here is the full document (PDF - 634 KB). For analysts, if the Petrobras price becomes very detached from the PPI again, the scenario of difficulty in supply could return, with new cuts in imports.",
#         "lang": "en",
#         "labels": ["negative","positive"]
#     }}
# headers = {
#     "Content-Type": "application/json",
#     "apikey": "65f3f982-8197-40d4-b30e-cb5d8a213d4b"
# }

# res = requests.request("POST", url, json=payload, headers=headers)
# print(res.json())
#labels, scores = res.json()["labels"], res.json()["scores"]

# OUTPUTS
#['negative', 'positive', 'neutral']
#[0.352, 0.335, 0.313]
#{'labels': ['negative', 'positive'], 'scores': [0.513, 0.487]}



text = "Gasoline and diesel oil prices are already at their highest levels in 2023 and are expected to rise further by the end of the year. The tendency, according to experts interviewed by Poder360, is for values to remain under pressure, mainly due to movements in the external scenario, such as restrictions in the supply of oil and increased demand. Last Tuesday (September 5), Russia and Saudi Arabia, two of the largest global powers in the sector, announced the maintenance of oil production cuts. The Arabs extended the daily supply reduction of 1 million barrels for another 3 months. The Russians cut exports by 300 thousand barrels per day. The tightness in oil supply directly impacts prices. It's the law of the market: with less product available, the price rises. The Brent barrel, which is the international reference, reached US$90.60 on Wednesday (September 6) - at the highest price since November 2022. The value of a barrel of oil is one of the main components in the formation of fuel prices . It started the year at US$82. On June 12, it reached the lowest level of the year: US$71.80. While supply is low, global demand should be stable or even growing. A lot depends on China's behavior. According to the managing partner of CBIE (Brazilian Infrastructure Center), Adriano Pires, the Chinese economy has grown, but not as much as the market expected. “What we should have is a scenario of increased fuel prices or stability, at least. The size of this depends largely on China's behavior. It is not possible, given the current situation, to project a reduction in prices, unless we see a slowdown in the global economy,” he stated. With expectations in China and other factors, analysts predicted a barrel of US$ 100 by the end of the year. This scenario currently seems less likely. “The exchange rate is stabilized, unless an extraordinary event occurs. The barrel is expected to grow in the 2nd half of the year, with restricted supply, inflation and growth of the Chinese economy, but we have to see the size of the growth”, says Pires. This scenario adds to the internal problems, which have already raised prices. Last week, diesel oil exceeded R$ 6. The average price of gasoline in the country was R$ 5.87, having for the 2nd week in a row the highest value recorded in the year by the ANP (National Petroleum and Petroleum Agency) survey. Natural gas). Due to high prices, the market is already projecting a reduction in gasoline consumption. For September, demand is expected to fall 3.4%, the first drop since the pandemic. The reason is the increase in ethanol consumption, which has become more competitive, says Amance Boutin, fuel specialist at Argus, a company that specializes in producing reports and analyzes for the fuel market. “The outlook for gasoline demand in Brazil for the rest of the year is downward, following an uninterrupted increase in consumption since Covid. Consumers are switching to hydrated ethanol, which is expected to increase consumption by 15%. The internal supply perspective does not change much. With the drop in demand, we should have more slack in supply,” he says. Diesel has a worse scenario. The case of diesel is the most delicate. The price has been climbing for 6 weeks and is now at its highest value since February. And it will rise further: last Tuesday (September 5), the government resumed charging federal taxes on fuel. The PIS/Cofins rate will be partial, but will increase progressively until January. “The current situation and in the coming months is a tightening of oil supply. But the global market still finds an ample supply of gasoline. In the case of diesel, it has a greater impact. The national supply capacity is already fully employed and you need to resort to external products. And there is a tendency for prices to rise in the international diesel market”, says Amance Boutin. The Argus expert recalls that part of the diesel imported by Brazil is Russian, which arrives in the country at a lower cost. “[This diesel] comes with a big discount for Brazil to be able to sell the product in large markets, as we have no restrictions here to bring Russian products. But with the extension of Russia's cut, this should impact the value of their diesel.” Diesel prices had been falling since the beginning of the year, which was accentuated after the announcement of the new policy by Petrobras (BVMF:PETR4), which abandoned the PPI (Import Parity Price) in May. It even dropped R$0.60 at the pumps from May to July alone. Since then, values have been rising every week. First, due to the internal supply crisis that reduced diesel stocks in the country due to the drop in imports. With the prices being charged by Petrobras, bringing fuel from abroad was not paying off. And around 25% of the diesel consumed in the country is imported. The result: some stations had difficulty purchasing. With little supply, prices rose. Then, there was the Petrobras adjustment, announced on August 15, which increased diesel prices at refineries by 25%. It resolved most of the gap, which, however, still persists. The current values of the state-owned company are 14% below international prices (it reached a 30% lag at the beginning of August), indicates a report by Abicom (Brazilian Association of Fuel Importers) released last Wednesday (September 6). Here is the full document (PDF - 634 KB). For analysts, if the Petrobras price becomes very detached from the PPI again, the scenario of difficulty in supply could return, with new cuts in imports."


from transformers import pipeline

model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
pipe = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path, max_length=512, truncation=True)

text = "Today was the best day of my life"
print(pipe(text))


# from transformers import AutoModelForSequenceClassification
# from transformers import TFAutoModelForSequenceClassification
# from transformers import AutoTokenizer, AutoConfig
# import numpy as np
# from scipy.special import softmax

# MODEL = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"

# tokenizer = AutoTokenizer.from_pretrained(MODEL)
# config = AutoConfig.from_pretrained(MODEL)

# # PT
# model = AutoModelForSequenceClassification.from_pretrained(MODEL, ignore_mismatched_sizes=True)
# model.save_pretrained(MODEL)
# tokenizer.save_pretrained(MODEL)

# text = 'I love you so much'
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
# scores = output[0][0].detach().numpy()
# scores = softmax(scores)

# # Print labels and scores
# ranking = np.argsort(scores)
# ranking = ranking[::-1]
# for i in range(scores.shape[0]):
#     l = config.id2label[ranking[i]]
#     s = scores[ranking[i]]
#     print(f"{i+1}) {l} {np.round(float(s), 4)}")
