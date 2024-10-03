import unittest
import enum


class Converter:
    class ConvertType(enum.Enum):
        GB_TO_MB = 1
        GHZ_TO_MHZ = 2
        KM_TO_M = 3
        KG_TO_G = 4

    @staticmethod
    def convert(convert_type: ConvertType, value):
        result = 0
        match convert_type:
            case Converter.ConvertType.GB_TO_MB:
                result = value * 1024
            case Converter.ConvertType.GHZ_TO_MHZ | Converter.ConvertType.KM_TO_M | Converter.ConvertType.KG_TO_G:
                result = value * 1000
        return result

    @staticmethod
    def batch_convert(convert_type: ConvertType, values):
        return [Converter.convert(convert_type, value) for value in values]


class TestConverter(unittest.TestCase):
    def test_GB_TO_MB(self):
        # Arrange
        input = 5
        ct = Converter.ConvertType.GB_TO_MB
        expected = 5120
        # Act
        result = Converter.convert(ct, input)
        # Assert
        self.assertEqual(expected, result)

    def test_GHZ_TO_MHZ(self):
        # Arrange
        input = 2
        ct = Converter.ConvertType.GHZ_TO_MHZ
        expected = 2000
        # Act
        result = Converter.convert(ct, input)
        # Assert
        self.assertEqual(expected, result)

    def test_KM_TO_M(self):
        # Arrange
        input = 4
        ct = Converter.ConvertType.KM_TO_M
        expected = 4000
        # Act
        result = Converter.convert(ct, input)
        # Assert
        self.assertEqual(expected, result)

    def test_KG_TO_G(self):
        # Arrange
        input = 2
        ct = Converter.ConvertType.KG_TO_G
        expected = 2000
        # Act
        result = Converter.convert(ct, input)
        # Assert
        self.assertEqual(expected, result)
