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
   Filename            : Main.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Main exposing (..)

import Models exposing (init_model, Flag, Model)
import Msgs exposing (Msg)
import Ports exposing (set_title)
import Routing exposing (delta2url, url2msgs)
import RouteUrl exposing (RouteUrlProgram)
import Update exposing (update)
import Views exposing (view)


-- Main --


main : RouteUrlProgram Flag Model Msg
main =
    RouteUrl.programWithFlags
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        , delta2url = delta2url
        , location2messages = url2msgs
        }



-- init --


init : Flag -> ( Model, Cmd Msg )
init flag =
    let
        model =
            init_model flag
    in
        ( model, set_title model.settings.title )



-- subscriptions --


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none
