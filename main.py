import asyncio
from agents.agent import Agent

async def main():
    a = Agent()
    rsp = await a.run(
    """
    	1.	检查材料：
	•	如果没有咖啡粉或水，则结束流程。
	2.	加热水：
	•	循环加热水直到温度达到90至96摄氏度。
	3.	冲泡咖啡：
	•	将咖啡粉放入咖啡机。
	•	倒入热水，等待4分钟。
	4.	检查咖啡是否准备好：
	•	如果咖啡未准备好，等待更长时间。
	•	如果咖啡准备好了，进行下一步。
	5.	享用咖啡：
	•	检查咖啡温度，如果适宜则享用。
    """
    )

if __name__ == "__main__":
    
    asyncio.run(main())