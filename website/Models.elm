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
   Filename            : Models.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Models exposing (..)

import Navigation exposing (Location)
import RemoteData exposing (WebData)


type alias Flag =
    Location


init_model : Flag -> Model
init_model flag =
    { blogs = RemoteData.Loading
    , blog = RemoteData.Loading
    , settings = { title = "Nasy Land", location = flag, route = Normal, nav = { f = True, n = False } }
    }


type alias Model =
    { blogs : WebData BlogsModel
    , blog : WebData BlogModel
    , settings : Settings
    }


type alias Date =
    { year : String, month : String, day : String }


type alias BlogModel =
    { title : String
    , author : String
    , summary : String
    , language : String
    , tags : List String
    , categories : List String
    , date : Date
    , datetime : String
    , wordcount : String
    , blog_path : String
    , id : String
    , last : String
    , last_name : String
    , next : String
    , next_name : String
    , content : String
    , content_table : String
    }


type alias BlogsModel =
    List BlogModel


type alias BlogPath =
    String


type alias Settings =
    { location : Location, title : String, route : Route, nav : { f : Bool, n : Bool } }


type Route
    = Normal
    | BlogRoute
    | NotFoundRoute
