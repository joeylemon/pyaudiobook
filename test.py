import unittest
import pyaudiobook


class TestHelpers(unittest.TestCase):
    def test_is_mp3_path(self):
        self.assertTrue(pyaudiobook.is_mp3_path("Chapter 1.mp3"))
        self.assertTrue(pyaudiobook.is_mp3_path("/home/user/audiobook/Chapter1.mp3"))
        self.assertFalse(pyaudiobook.is_mp3_path("/home/user/audiobook/chapter1.jpg"))
        self.assertFalse(pyaudiobook.is_mp3_path("chapter1.mp4"))

    def test_get_track_num(self):
        self.assertEqual(pyaudiobook.get_track_num("/home/user/audiobook/Chapter 1 - Test.mp3"), 1)
        self.assertEqual(pyaudiobook.get_track_num("/home/user/audiobook/Chapter 01 - Test.mp3"), 1)
        self.assertEqual(pyaudiobook.get_track_num("/home/user/audiobook/Chapter1 - Test.mp3"), 1)
        self.assertEqual(pyaudiobook.get_track_num("/home/user/audiobook/Chapter01 - Test.mp3"), 1)
        self.assertEqual(pyaudiobook.get_track_num("/home/user/audiobook/Track1 - Test.mp3"), 1)
        self.assertEqual(pyaudiobook.get_track_num("/home/user/audiobook/Chapter 15 - Test.mp3"), 15)
        self.assertEqual(pyaudiobook.get_track_num("056 - Hitchhikers Guide To The Galaxy Pt 56 Of 66.mp3"), 56)
        self.assertRaises(ValueError, pyaudiobook.get_track_num, "/home/user/audiobook/Chapter I - Test.mp3")


if __name__ == "__main__":
    unittest.main()
