from django.test import TestCase
from django.urls import reverse 
from .models import BlogPost, Image

class AnnouncementsTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        cls.blogpost = BlogPost.objects.create(
        cover = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        video = "https://www.youtube.com/embed/tgbNymZ7vqY",
        title = "Jay Doeseee this work ?",
        body = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque eu quam sed",
        post_type="announcement",)

        cls.image = Image.objects.create(
            post= cls.blogpost,
            image = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        )

        cls.blogpost2 = BlogPost.objects.create(
        cover = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        video = "https://www.youtube.com/embed/tgbNymZ7vqY",
        title = "Jay Does this work ?",
        body = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque eu quam sed",
        post_type="announcement",
        latest = True,
        )

        cls.image2 = Image.objects.create(
            post= cls.blogpost2,
            image = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        )


    def test_main_page_status_code(self):
        response = self.client.get(reverse("announcements"))
        self.assertEqual(response.status_code,200)

    def test_main_page_uses_correct_template(self):
        response = self.client.get(reverse("announcements"))
        self.assertTemplateUsed(response,"main.html")

    def test_main_page_shows_latest_post(self):
        response = self.client.get(reverse("announcements"))
        self.assertContains(response,"Jay Does this work ?")
        self.assertNotContains(response,"isn't here")


    def test_main_page_contains_cover_for_latest_post(self):
        response = self.client.get(reverse("announcements"))
        self.assertContains(response, self.blogpost.cover)

    
    def test_main_page_contains_video_for_latest_post(self):
        response = self.client.get(reverse("announcements"))
        self.assertContains(response, self.blogpost.video)


    def test_main_page_shows_other_posts(self):
        response = self.client.get(reverse("announcements"))
        self.assertContains(response,"Jay Doeseee this work ?")
        self.assertNotContains(response,"isn't here")

    def test_main_page_contains_cover_for_other_posts(self):
        response = self.client.get(reverse("announcements"))
        self.assertContains(response, self.blogpost2.cover)



class PostDetailTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.blogpost = BlogPost.objects.create(
        cover = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        video = "https://www.youtube.com/embed/tgbNymZ7vqY",
        title = "Jay Doeseee this work ?",
        body = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque eu quam sed",
        post_type="announcement",)

        cls.image = Image.objects.create(
            post= cls.blogpost,
            image = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        )

    def test_post_page_status_code(self):
        response = self.client.get(self.blogpost.get_absolute_url())
        self.assertEqual(response.status_code,200)

    def test_post_page_uses_correct_template(self):
        response = self.client.get(self.blogpost.get_absolute_url())
        self.assertTemplateUsed(response,"post_detail.html")

    def test_post_page_shows_post(self):
        response = self.client.get(self.blogpost.get_absolute_url())
        self.assertContains(response,"Jay Doeseee this work ?")
        self.assertNotContains(response,"isn't here")    

    def test_post_page_contains_image(self):
        response = self.client.get(self.blogpost.get_absolute_url())
        self.assertContains(response, self.image.image)


class SoonTemplateTest(TestCase):
    
    def test_soon_status_code(self):
        response = self.client.get(reverse("soon"))
        self.assertEqual(response.status_code,200)

    def test_soon_status_code(self):
        response = self.client.get(reverse("soon"))
        self.assertTemplateUsed(response,"soon.html")

class AboutTemplateTest(TestCase):
    
    def test_about_status_code(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)

    def test_soon_status_code(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response,"about.html")


class GameListTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.blogpost = BlogPost.objects.create(
        cover = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        video = "https://www.youtube.com/embed/tgbNymZ7vqY",
        title = "Jay Doeseee this work ?",
        body = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque eu quam sed",
        post_type="announcement",)

        cls.image = Image.objects.create(
            post= cls.blogpost,
            image = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        )

        cls.blogpost2 = BlogPost.objects.create(
        cover = "https://i.ibb.co/8B9m3GR/My-Portfolio.png",
        video = "https://www.youtube.com/embed/tgbNymZ7vqY",
        title = "Jay Does this work ?",
        body = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque eu quam sed",
        post_type="announcement",
        latest = True,
        )        

    def test_games_status_code(self):
        response = self.client.get(reverse("games"))
        self.assertEqual(response.status_code,200)

    def test_games_status_code(self):
        response = self.client.get(reverse("games"))
        self.assertTemplateUsed(response,"games.html")

    def test_games_contains_games(self):
        response = self.client.get(reverse("games"))
        self.assertContains(response,"Jay Does this work ?")
        self.assertContains(response,"Jay Doeseee this work ?")

    def test_games_contains_covers(self):
        response = self.client.get(reverse("games"))
        self.assertContains(response,self.blogpost.cover)
        self.assertContains(response,self.blogpost2.cover)


