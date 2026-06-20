import func
from plyer import notification





while True:
   print("\n🐾 ===== Pet Care System ===== 🐾")
   print("1️⃣ Add Pet")
   print("2️⃣ View Pets")
   print("3️⃣ Delete Pet")
   print("4️⃣ Vaccination Check")
   print("5️⃣ Feed Pet")
   print("6️⃣ Exit")
   user_choice=int(input("Enter Your choice (1-6):"))

   if user_choice==1:
        func.add_pet()
   elif user_choice==2:
        func.view_pets()
   elif user_choice==3:
        func.delete_pets()
   elif user_choice==4:
        func.check_vaccination()
   elif user_choice==5:
        func.pet_feed()
   elif user_choice==6:
        print("Goodbye! 👋")
        break
   else:
        print("Invalid choice, try again.")
    
