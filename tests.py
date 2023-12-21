from unittest.mock import patch
from unittest import TestCase, main
from main import parse_range, scan_ports
from typing import List
from testhelper import capture
import socket
import main


class TestParseRange(TestCase):
    def test_parse_range_valid_input(self):
        self.assertEqual(parse_range("0-400"), (0, 400))

    def test_parse_range_invalid_input_no_hyphen(self):
        with self.assertRaises(ValueError):
            parse_range("0400")

    def test_parse_range_invalid_input_string_with_hyphen(self):
        with self.assertRaises(ValueError):
            parse_range("Hello-World")

    def test_parse_range_invalid_input_empty(self):
        with self.assertRaises(ValueError):
            parse_range("")

    def test_parse_range_invalid_input_none(self):
        with self.assertRaises(AttributeError):
            parse_range(None)

    def test_parse_range_invalid_input_int(self):
        with self.assertRaises(AttributeError):
            parse_range(1)

    @patch("main.socket")
    def test_scan_ports_all_closed(self, mock_socket):
        ip = "31.58.249.81"
        start = 0
        stop = 10

        mock_socket.return_value.connect_ex.return_value = 1

        result = scan_ports(ip, start, stop)

        self.assertEqual(result, 0)

    @patch("main.socket")
    def test_scan_ports_cli_all_open(self, mock_socket):
        ip = "31.58.249.81"
        start = 0
        stop = 10

        mock_socket.return_value.connect_ex.return_value = 0

        result = scan_ports(ip, start, stop)

        self.assertEqual(result, 11)
