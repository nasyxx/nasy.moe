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
   Filename            : Commands.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Commands exposing (..)

import Http
import Json.Decode as Decode exposing (field, list, string)
import Json.Decode.Pipeline exposing (decode, required, optional)
import Msgs exposing (Msg)
import Models exposing (BlogsModel, BlogModel, Date)
import RemoteData


-- Decoders --


date_decoder : Decode.Decoder Date
date_decoder =
    decode Date
        |> required "year" string
        |> required "month" string
        |> required "day" string


main_decoder : Decode.Decoder BlogModel
main_decoder =
    decode BlogModel
        |> required "title" string
        |> required "author" string
        |> required "summary" string
        |> required "language" string
        |> required "tags" (list string)
        |> required "categories" (list string)
        |> required "date" date_decoder
        |> required "datetime" string
        |> required "wordcount" string
        |> required "blog_path" string
        |> required "id" string
        |> optional "content" string ""
        |> optional "content_table" string ""


blog_decoder : Decode.Decoder BlogModel
blog_decoder =
    main_decoder |> field "results"


blogs_decoder : Decode.Decoder BlogsModel
blogs_decoder =
    list main_decoder |> field "results"



-- Fetcher --


blog_url : String
blog_url =
    "http://new.nasy.moe:1314/blog/"


blogs_url : String
blogs_url =
    "http://new.nasy.moe:1314/blogs"


fetch_blogs : Cmd Msg
fetch_blogs =
    Http.get blogs_url blogs_decoder
        |> RemoteData.sendRequest
        |> Cmd.map Msgs.OnFetchBlogs


fetch_blog : String -> Cmd Msg
fetch_blog blog_path =
    Http.get (blog_url ++ blog_path) blog_decoder
        |> RemoteData.sendRequest
        |> Cmd.map Msgs.OnFetchBlog
