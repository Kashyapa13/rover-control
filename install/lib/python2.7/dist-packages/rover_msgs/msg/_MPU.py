# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rover_msgs/MPU.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MPU(genpy.Message):
  _md5sum = "2c0239ab8497dbf714abae1bc9165695"
  _type = "rover_msgs/MPU"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 gyro_x
float32 gyro_y
float32 gyro_z
float32 acc_x
float32 acc_y
float32 acc_z
"""
  __slots__ = ['gyro_x','gyro_y','gyro_z','acc_x','acc_y','acc_z']
  _slot_types = ['float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MPU, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.gyro_x is None:
        self.gyro_x = 0.
      if self.gyro_y is None:
        self.gyro_y = 0.
      if self.gyro_z is None:
        self.gyro_z = 0.
      if self.acc_x is None:
        self.acc_x = 0.
      if self.acc_y is None:
        self.acc_y = 0.
      if self.acc_z is None:
        self.acc_z = 0.
    else:
      self.gyro_x = 0.
      self.gyro_y = 0.
      self.gyro_z = 0.
      self.acc_x = 0.
      self.acc_y = 0.
      self.acc_z = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_6f.pack(_x.gyro_x, _x.gyro_y, _x.gyro_z, _x.acc_x, _x.acc_y, _x.acc_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.gyro_x, _x.gyro_y, _x.gyro_z, _x.acc_x, _x.acc_y, _x.acc_z,) = _struct_6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_6f.pack(_x.gyro_x, _x.gyro_y, _x.gyro_z, _x.acc_x, _x.acc_y, _x.acc_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.gyro_x, _x.gyro_y, _x.gyro_z, _x.acc_x, _x.acc_y, _x.acc_z,) = _struct_6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6f = struct.Struct("<6f")
