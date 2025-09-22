import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL             
                 )
''')


def list_videos():
   cursor.execute("SELECT * FROM videos")
   for row in cursor.fetchall():
      print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
   cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name,new_time,video_id))
   conn.commit()

def delete_video(video_id):
   cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
   conn.commit()




def main():
    while True:
       print("1. List Videos")
       print("2. Add Videos ")
       print("3. Update Videos ")
       print("4. Delete Videos ")
       print("5. Exit ")
       action  = input("Enter Your Choice!: ")

       if action == '1':
           list_videos()
       elif action == '2':
          name = input("Enter the video Name: ")
          time = input("Enter the video Time: ")
          add_video(name,time)
       elif action == '3':
          video_id = input("Enter Video Id: ")
          name = input("Enter the video Name: ")
          time = input("Enter the video Time: ")
          update_video(video_id,name,time)
       elif action == '4':
          video_id = input("Enter Video Id to delete: ")
          delete_video(video_id)
       elif action == '5':
          break
       else:
          print("INVALID CHOICE!")
    conn.close()









if __name__ == "__main__":
  main()