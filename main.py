def show_menu():
  print("====== AI金融助手 ======")
  print("1.理财需求分析")
  print("2.基金需求分析")
  print("3.退出系统")

def analyze_financial_needs(user_input):
    found = False

    if "低风险" in user_input:
         print("客户偏好：稳健型")
         print("建议中低风险产品")
         found = True

    if "半年" in user_input:
         print("推荐期限:6个月左右")
         found = True

    if "高收益" in user_input:
         print("客户偏好：进取型")
         print("建议先评估客户的风险承受能力")
         found = True

    if found == False:
         print("客户偏好：未知")
    print("风险提示：投资有风险，入市需谨慎")
while True:
  
  show_menu()

  choice = input("请选择功能:")

  if choice == "1":
     
    txt = input("请输入客户需求： ")
    
    analyze_financial_needs(txt)
     

  elif choice == "2":
    print("基金需求分析功能正在开发中...")
  
  elif choice == "3":
    print("退出系统")
    break
  else:
    print("无效选择，请重新输入")    
    
       