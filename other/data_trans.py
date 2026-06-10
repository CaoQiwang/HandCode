import json


with open("sft_data.jsonl", "r", encoding="utf-8") as f_in, \
     open("chatml_data.jsonl", "w", encoding="utf-8") as f_out:
    for line in f_in:
        item = json.loads(line)
        user_text = item.get("instruction", "") + ("\n" + item["input"] if item.get("input") else "")
        assistant_text = item.get("output", "")
        chatml = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_text},
                {"role": "assistant", "content": assistant_text}
            ]
        }
        f_out.write(json.dumps(chatml, ensure_ascii=False) + "\n")