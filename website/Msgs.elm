{-
   Excited without bugs, have fun ("▔□▔)/hi~♡ Nasy.
   -----------------------------------------------
   |
   |             *         *
   |                  .                .
   |           .
   |     *                      ,
   |                   .
   |
   |                               *
   |          |\___/|
   |          )    -(             .              '
   |         =\  -  /=
   |           )===(       *
   |          /   - \
   |          |-    |
   |         /   -   \     0.|.0
   |  NASY___\__( (__/_____(\=/)__+1s____________
   |  ______|____) )______|______|______|______|_
   |  ___|______( (____|______|______|______|____
   |  ______|____\_|______|______|______|______|_
   |  ___|______|______|______|______|______|____
   |  ______|______|______|______|______|______|_
   |  ___|______|______|______|______|______|____

   -----------------------------------------------

   Author              : Nasy https://nasy.moe <Nasy>
   Date                : Mar 10, 2018
   Email               : echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
   Filename            : Msgs.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Msgs exposing (..)

import Models exposing (BlogModel, BlogsModel)
import RemoteData exposing (WebData)


type Msg
    = OnFetchBlog (WebData BlogModel)
    | OnFetchBlogs (WebData BlogsModel)
    | SetUrl String
    | OnLocationChange
    | ChangeNavF
    | ChangeNavN
    | Up2Top
    | InitComment
