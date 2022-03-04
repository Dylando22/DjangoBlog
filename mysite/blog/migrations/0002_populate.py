
from django.db import migrations
from django.utils import timezone

def populate_db(apps, schema_editor):

    Blog = apps.get_model('blog', 'BlogPost')
    Blog.objects.all().delete()

    Comment = apps.get_model('blog', 'Comment')
    Comment.objects.all().delete()

    Loki_post = Blog(title="Loki's Birthday",
                     author="Dylan Spencer",
                     content="Today we got a new puppy named Loki! He is so cute! He is a cavapoochon and is very mischievous. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                     posted="2021-11-22 20:52:55",
                     comment_count=4,)
    Loki_post.save()

    Vacation_post = Blog(title="Vacation Day",
                     author="Dylan Spencer",
                     content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet nisl suscipit adipiscing bibendum est ultricies integer quis. Semper quis lectus nulla at. In massa tempor nec feugiat nisl pretium fusce id. Pellentesque elit eget gravida cum sociis natoque penatibus et. Sit amet volutpat consequat mauris nunc congue nisi vitae. Quis eleifend quam adipiscing vitae proin sagittis nisl. Netus et malesuada fames ac turpis egestas sed tempus urna. Amet purus gravida quis blandit. Scelerisque purus semper eget duis at tellus at urna condimentum. Morbi tristique senectus et netus et malesuada fames ac turpis. Pharetra diam sit amet nisl suscipit adipiscing bibendum est. Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Egestas egestas fringilla phasellus faucibus scelerisque eleifend. Vulputate dignissim suspendisse in est ante in. Pharetra et ultrices neque ornare aenean euismod elementum nisi. Ullamcorper malesuada proin libero nunc consequat interdum varius. Faucibus purus in massa tempor nec feugiat. Magna fermentum iaculis eu non diam phasellus vestibulum lorem. Nibh tellus molestie nunc non. Urna cursus eget nunc scelerisque viverra mauris in aliquam. Sit amet aliquam id diam maecenas ultricies mi eget mauris. Dui sapien eget mi proin sed libero enim sed. Aliquam vestibulum morbi blandit cursus risus at ultrices. Imperdiet dui accumsan sit amet nulla facilisi morbi. Quam id leo in vitae. At in tellus integer feugiat scelerisque varius. Consectetur adipiscing elit ut aliquam purus sit amet luctus venenatis. Amet nisl suscipit adipiscing bibendum est. Non quam lacus suspendisse faucibus interdum.\n\n Interdum consectetur libero id faucibus nisl tincidunt eget nullam non. Euismod elementum nisi quis eleifend quam adipiscing vitae proin. Et malesuada fames ac turpis egestas integer. Tincidunt ornare massa eget egestas purus viverra accumsan in. Cursus sit amet dictum sit amet justo donec enim. Purus viverra accumsan in nisl nisi scelerisque eu. Massa sed elementum tempus egestas sed.",
                     posted="2021-10-22 20:52:55",
                     comment_count = 1)

    Vacation_post.save()


    RoseBowl_post = Blog(title="Rose Bowl",
                         author="Dylan Spencer",
                         content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet nisl suscipit adipiscing bibendum est ultricies integer quis. Semper quis lectus nulla at. In massa tempor nec feugiat nisl pretium fusce id. Pellentesque elit eget gravida cum sociis natoque penatibus et. Sit amet volutpat consequat mauris nunc congue nisi vitae. Quis eleifend quam adipiscing vitae proin sagittis nisl. Netus et malesuada fames ac turpis egestas sed tempus urna. Amet purus gravida quis blandit. Scelerisque purus semper eget duis at tellus at urna condimentum. Morbi tristique senectus et netus et malesuada fames ac turpis. Pharetra diam sit amet nisl suscipit adipiscing bibendum est. Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Egestas egestas fringilla phasellus faucibus scelerisque eleifend. Vulputate dignissim suspendisse in est ante in. Pharetra et ultrices neque ornare aenean euismod elementum nisi. Ullamcorper malesuada proin libero nunc consequat interdum varius. Faucibus purus in massa tempor nec feugiat. Magna fermentum iaculis eu non diam phasellus vestibulum lorem. Nibh tellus molestie nunc non. Urna cursus eget nunc scelerisque viverra mauris in aliquam. Sit amet aliquam id diam maecenas ultricies mi eget mauris. Dui sapien eget mi proin sed libero enim sed. Aliquam vestibulum morbi blandit cursus risus at ultrices. Imperdiet dui accumsan sit amet nulla facilisi morbi. Quam id leo in vitae. At in tellus integer feugiat scelerisque varius. Consectetur adipiscing elit ut aliquam purus sit amet luctus venenatis. Amet nisl suscipit adipiscing bibendum est. Non quam lacus suspendisse faucibus interdum.\n\n Interdum consectetur libero id faucibus nisl tincidunt eget nullam non. Euismod elementum nisi quis eleifend quam adipiscing vitae proin. Et malesuada fames ac turpis egestas integer. Tincidunt ornare massa eget egestas purus viverra accumsan in. Cursus sit amet dictum sit amet justo donec enim. Purus viverra accumsan in nisl nisi scelerisque eu. Massa sed elementum tempus egestas sed.",
                         posted="2022-01-01 05:55:55",
                         comment_count=1 )

    RoseBowl_post.save()


    Anniversary_post = Blog(title="Anniversary",
                            author="Savannah Spencer",
                            content="The time had come for Nancy to say goodbye. She had been dreading this moment for a good six months, and it had finally arrived despite her best efforts to forestall it. No matter how hard she tried, she couldn't keep the inevitable from happening. So the time had come for a normal person to say goodbye and move on. It was at this moment that Nancy decided not to be a normal person. After all the time and effort she had expended, she couldn't bring herself to do it.\n\nI recollect that my first exploit in squirrel-shooting was in a grove of tall walnut-trees that shades one side of the valley. I had wandered into it at noontime, when all nature is peculiarly quiet, and was startled by the roar of my own gun, as it broke the Sabbath stillness around and was prolonged and reverberated by the angry echoes.\n\nThe red ball sat proudly at the top of the toybox. It had been the last to be played with and anticipated it would be the next as well. The other toys grumbled beneath. At one time each had held the spot of the red ball, but over time they had sunk deeper and deeper into the toy box.",
                            posted="2021-05-28 12:24:09")

    Anniversary_post.save()

    co0 = Comment(blog=Loki_post,
                  commenter="Sam",
                  content="This is a great post",
                  email="abc@123.org",
                  posted="2021-11-22 23:52:55")
    co0.save()

    co1 = Comment(blog=Loki_post,
              commenter="Jimmy",
              content="I agree",
              email="def@123.org",
              posted="2021-11-22 23:55:55")
    co1.save()

    co2 = Comment(blog=Loki_post,
              commenter="Sally",
              content="So cute!!",
              email="fefef@123.org",
              posted="2021-11-22 23:57:55")
    co2.save()

    co3 = Comment(blog=Loki_post,
              commenter="Savannah",
              content="we love him so much!",
              email="fsavvyf@123.org",
              posted="2021-11-22 23:59:55")
    co3.save()

    comm = Comment(blog=RoseBowl_post,
            commenter="Ute Fan",
            content="Can't believe we lost...",
            email="utahman@hotmail.com",
            posted="2022-01-02 15:59:43")

    comm.save()

    ci = Comment(blog=Vacation_post,
            commenter="Wife",
            content="Love you babe!",
            email="lovers@hotmail.com",
            posted="2021-10-23 06:22:55")
    ci.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
