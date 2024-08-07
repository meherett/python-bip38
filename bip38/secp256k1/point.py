#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Any
from ecdsa.ecdsa import curve_secp256k1
from ecdsa.ellipticcurve import (
    Point as _Point, PointJacobi
)
from ecdsa import keys

from ..const import SECP256K1
from ..utils import (
    bytes_to_integer, integer_to_bytes
)


class Point:

    point: PointJacobi

    def __init__(self, point_obj: PointJacobi) -> None:
        """
        Initializes the class with a PointJacobi object.

        :param point_obj: The PointJacobi object representing the point.
        :type point_obj: PointJacobi
        """
        self.point = point_obj

    @classmethod
    def from_bytes(cls, point: bytes) -> "Point":
        """
        Creates a point from its byte representation.

        :param point: The byte representation of the point.
        :type point: bytes

        :return: An instance of IPoint representing the decoded point.
        :rtype: IPoint
        """

        try:
            return cls(
                PointJacobi.from_bytes(
                    curve_secp256k1, point
                )
            )
        except keys.MalformedPointError as ex:
            raise ValueError("Invalid point key bytes") from ex
        except AttributeError:
            return cls.from_coordinates(
                bytes_to_integer(point[:SECP256K1.POINT_COORDINATE_BYTE_LENGTH]),
                bytes_to_integer(point[SECP256K1.POINT_COORDINATE_BYTE_LENGTH:])
            )

    @classmethod
    def from_coordinates(cls, x: int, y: int) -> "Point":
        """
        Creates a point from x and y.

        :param x: The x of the point.
        :type x: int
        :param y: The y of the point.
        :type y: int

        :return: An instance of IPoint representing the point with the given coordinates.
        :rtype: IPoint
        """

        return cls(
            PointJacobi.from_affine(
                _Point(curve_secp256k1, x, y)
            )
        )

    def underlying_object(self) -> Any:
        """
        Returns the underlying point object.

        :return: The underlying point object.
        :rtype: Any
        """

        return self.point

    def x(self) -> int:
        """
        Returns the x of the point.

        :return: The x of the point.
        :rtype: int
        """

        return self.point.x()

    def y(self) -> int:
        """
        Returns the y of the point.

        :return: The y of the point.
        :rtype: int
        """

        return self.point.y()

    def raw(self) -> bytes:
        """
        Returns the raw bytes representation of the point.

        :return: The raw bytes representation of the point.
        :rtype: bytes
        """

        return self.raw_decoded()

    def raw_encoded(self) -> bytes:
        """
        Returns the raw encoded bytes of the point.

        :return: The raw encoded bytes of the point.
        :rtype: bytes
        """

        try:
            return self.point.to_bytes("compressed")
        except AttributeError:
            x: bytes = integer_to_bytes(self.point.x(), SECP256K1.POINT_COORDINATE_BYTE_LENGTH)
            return b"\x03" + x if self.point.y() & 1 else b"\x02" + x

    def raw_decoded(self) -> bytes:
        """
        Returns the raw decoded bytes of the point.

        :return: The raw bytes of the point.
        :rtype: bytes
        """

        try:
            return self.point.to_bytes()
        except AttributeError:
            x: bytes = integer_to_bytes(self.point.x(), SECP256K1.POINT_COORDINATE_BYTE_LENGTH)
            y: bytes = integer_to_bytes(self.point.y(), SECP256K1.POINT_COORDINATE_BYTE_LENGTH)

            return x + y

    def __add__(self, point: "Point") -> "Point":
        """
        Performs addition with another point.

        :param point: The point to add.
        :type point: IPoint

        :return: A new instance of the class representing the result of the addition.
        :rtype: IPoint
        """

        return self.__class__(self.point + point.underlying_object())

    def __radd__(self, point: "Point") -> "Point":
        """
        Performs addition with another point in the context of scalar multiplication.

        :param point: The point to add (right operand).
        :type point: IPoint

        :return: A new instance of the class representing the result of the addition.
        :rtype: IPoint
        """

        return self + point

    def __mul__(self, scalar: int) -> "Point":
        """
        Performs scalar multiplication on the point.

        :param scalar: The scalar value to multiply with the point.
        :type scalar: int

        :return: A new instance of the class representing the result of scalar multiplication.
        :rtype: IPoint
        """

        return self.__class__(self.point * scalar)

    def __rmul__(self, scalar: int) -> "Point":
        """
        Performs scalar multiplication on the point.

        :param scalar: The scalar value to multiply with the point.
        :type scalar: int

        :return: The result of scalar multiplication.
        :rtype: IPoint
        """

        return self * scalar
