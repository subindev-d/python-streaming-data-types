# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class DimensionMetaData(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsDimensionMetaData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DimensionMetaData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def DimensionMetaDataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x68\x73\x30\x31", size_prefixed=size_prefixed
        )

    # DimensionMetaData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DimensionMetaData
    def Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # DimensionMetaData
    def Unit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # DimensionMetaData
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # DimensionMetaData
    def BinBoundariesType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # DimensionMetaData
    def BinBoundaries(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None


def DimensionMetaDataStart(builder):
    builder.StartObject(5)


def DimensionMetaDataAddLength(builder, length):
    builder.PrependInt32Slot(0, length, 0)


def DimensionMetaDataAddUnit(builder, unit):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(unit), 0
    )


def DimensionMetaDataAddLabel(builder, label):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0
    )


def DimensionMetaDataAddBinBoundariesType(builder, binBoundariesType):
    builder.PrependUint8Slot(3, binBoundariesType, 0)


def DimensionMetaDataAddBinBoundaries(builder, binBoundaries):
    builder.PrependUOffsetTRelativeSlot(
        4, flatbuffers.number_types.UOffsetTFlags.py_type(binBoundaries), 0
    )


def DimensionMetaDataEnd(builder):
    return builder.EndObject()
