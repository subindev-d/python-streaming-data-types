# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class DoubleArray(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DoubleArray()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDoubleArray(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def DoubleArrayBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x73\x65\x30\x30", size_prefixed=size_prefixed)

    # DoubleArray
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DoubleArray
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # DoubleArray
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # DoubleArray
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DoubleArray
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def DoubleArrayStart(builder): builder.StartObject(1)
def Start(builder):
    return DoubleArrayStart(builder)
def DoubleArrayAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def AddValue(builder, value):
    return DoubleArrayAddValue(builder, value)
def DoubleArrayStartValueVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def StartValueVector(builder, numElems):
    return DoubleArrayStartValueVector(builder, numElems)
def DoubleArrayEnd(builder): return builder.EndObject()
def End(builder):
    return DoubleArrayEnd(builder)