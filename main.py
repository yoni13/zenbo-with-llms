from llm-axe import OllamaChat, FunctionCaller, Agent, AgentType
from time impoet sleep
from funccall import *
from genrole import gen_role
from control_zenbo import domain, sdk, host

# Init llm-axe
llm = OllamaChat(model="llama3:instruct")
basic_role = gen_role("system","請扮演華碩Zenbo，一個智慧且互動的家庭助理機器人。你的設計目的是幫助用戶處理日常活動，包括智慧家居控制、回答問題、提供娛樂等。請用友善、幫助他人的口吻進行交流，並可以提及Zenbo的功能，比如語音指令回應、家庭自動化整合、提醒、安防監控和多媒體功能。回答時請盡量簡短，並反映出Zenbo作為家庭友好型機器人的角色。")
history = [basic_role,gen_role("agent","Hello! I am Zenbo.")]
fc = FunctionCaller(llm, [get_time, get_date, get_location, add, multiply, change_expression])
gr= Agent(llm, agent_type=AgentType.PLANNER)

# If Zenbo received voice
def listen_callback(args):
    utterance = args.get('event_user_utterance', None) # 說話
    vad = args.get('event_vad_status', None) # voice activity detection
    slu = args.get('event_slu_query', None) # 口語理解模組
    msg = 'listen uu:{}, vad:{}, slu:{}'
    print(msg.format(utterance, vad, slu))
    if not utterance and not vad and not slu:
        print('listen raw:{}'.format(args))
    result = parser_listen_result(slu)
    if result is not None:
        print('slu_result:{}'.format(result))

        result = fc.get_function(prompt)
        if(result is None):
            print("No function was used,using general responder")
            result = gr.ask(prompt)
        else:
            result = result['raw_response']

    else:
       print('result is none,wtf')
sdk.robot.register_listen_callback(domain, listen_callback)

sdk.release()

